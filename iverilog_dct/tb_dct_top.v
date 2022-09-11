`timescale 1ns/1ps
`include "./dct_top.v"

module tp_dct_top();

reg clk, rst, enb;
reg [7:0] data_in;
reg [7:0] data_65536 [0:65536];
reg [7:0] data_out_reg;
wire [11:0] data_out;
wire tp_enb;

dct_top TEST(data_out, data_in, clk, rst, enb);

integer i, j, k;
integer f;

initial begin
    f = $fopen("data_2d_out.txt");
    #1490
    for (j=0;j<65536;j=j+1) begin
        // data_out_reg <= data_out;
        $fwrite(f, "%12b\n", data_out);
        k = j / 8;
        #(10);
    end
    $fclose(f);
end

initial begin
    rst <= 1;
    clk <= 1;
    enb <= 0;
    $readmemb("./data1.txt", data_65536);
    #11
    rst <= 0;
    #9
    for (i=0;i<65536;i=i+1) begin
        data_in <= data_65536[i];
        #(10);
        enb <= 1;
    end
    #1470
    $finish;
end

// icarus verilog part
initial begin
    $dumpfile("test_out.vcd");
    $dumpvars(-1, TEST);
end

always #5 clk <= ~clk;

endmodule