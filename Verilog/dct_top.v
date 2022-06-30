module dct_top(
    output [11:0] dct_data_out,
    input  [7:0]  dct_data_in,
    input  clk, rst, enb
);

parameter BWo1d = 10;
parameter BWo2d = 12;

reg [7:0] dct_data_in_reg;

wire [BWo1d-1:0] dct_1d_out, tp_1d_out;
wire [BWo2d-1:0] dct_2d_out, tp_2d_out;
wire tp_1d_enb, tp_2d_enb;
wire dct_2d_enb, dct_fin_enb;

dct_1d DCT1D(dct_1d_out, tp_1d_enb, dct_data_in_reg, clk, rst, enb);
tp_mem #(.BW(10)) TP1D(tp_1d_out, dct_2d_enb, dct_1d_out, clk, rst, tp_1d_enb);

dct_2d DCT2D(dct_2d_out, tp_2d_enb, tp_1d_out, clk, rst, dct_2d_enb);
tp_mem #(.BW(12)) TP2D(tp_2d_out, dct_fin_enb, dct_2d_out, clk, rst, tp_2d_enb);

assign dct_data_out = tp_2d_out;

always @ (posedge clk) begin
    if (rst) begin
        dct_data_in_reg <= 8'b0;
    end
    else begin
        dct_data_in_reg <= dct_data_in;
    end
end

endmodule
