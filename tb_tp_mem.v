`timescale 1ns/1ps

module tb_tp_mem();

reg clk, rst;
reg [7:0] data_in;
wire [7:0] data_out;

tp_mem tp_TEST(data_out, data_in, clk, rst, 1'b1);

integer i, j;

initial begin
    rst <= 1;
    clk <= 1;
    #11
    rst <= 0;
    #9
    for (i=0;i<4;i=i+1) begin
        for (j=0;j<64;j=j+1) begin
            data_in <= j;
            #(10);
        end
    end
end

always #5 clk <= ~clk;

endmodule