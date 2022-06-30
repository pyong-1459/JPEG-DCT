`timescale 1ns/1ps

module tb_dct_1d();

reg clk, rst, enb;
reg [7:0] data_in;
reg [7:0] data_65536 [0:65536];
reg [7:0] data_out_reg;
wire [9:0] data_out;
wire tp_enb;

dct_1d dctTEST(data_out, tp_enb, data_in, clk, rst, enb);

integer i, j, k;
integer f;

initial begin
    f = $fopen("data_1d_out.txt");
    #110
    for (j=0;j<65536;j=j+1) begin
        // data_out_reg <= data_out;
        $fwrite(f, "%10b\n", data_out);
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
    enb <= 1;
    #9
    for (i=0;i<65536;i=i+1) begin
        data_in <= data_65536[i];
        #(10);
    end
    #90
    $finish;
end

always #5 clk <= ~clk;

endmodule