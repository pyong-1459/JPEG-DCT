module dct_2d
#(  parameter BWo = 12,
    parameter BWi = 10)
(
    output [BWo-1:0] dct_out,
    output tp_mem_enb,
    input  [BWi-1:0] dct_in, // BWi
    input  clk, rst, enb
);

reg signed [BWi-1:0] data_10bx8 [0:7];
reg signed [BWo-1:0] data_outs [0:7];
reg [2:0] cnt_data, cnt_data_out;
reg tp_enb, tp_enb_delayed;

wire signed [BWi:0] v0, v1, v2, v3, v4, v5, v6, v7;
wire signed [BWi+1:0] v8, v9, v10, v11, v12, vv13, v14;
wire signed [BWi+2:0] v15, v16, vv17, vv18;
wire signed [BWi+3:0] v13;
wire signed [BWi+3:0] v17, v18, v19, v20, v21, v22, v23, v24;
wire signed [BWi+3:0] v25, v26, v27, v28;
// wire signed [11:0] v13;
wire signed [BWi+3:0] out1, out2, out3, out4, out5, out6, out7;

assign v0 = (|cnt_data) ?  10'b0 : ({data_10bx8[0][BWi-1], data_10bx8[0]} + {data_10bx8[7][BWi-1], data_10bx8[7]}); // 9
assign v1 = (|cnt_data) ?  10'b0 : ({data_10bx8[1][BWi-1], data_10bx8[1]} + {data_10bx8[6][BWi-1], data_10bx8[6]}); // 9
assign v2 = (|cnt_data) ?  10'b0 : ({data_10bx8[2][BWi-1], data_10bx8[2]} + {data_10bx8[5][BWi-1], data_10bx8[5]}); // 9
assign v3 = (|cnt_data) ?  10'b0 : ({data_10bx8[3][BWi-1], data_10bx8[3]} + {data_10bx8[4][BWi-1], data_10bx8[4]}); // 9
assign v4 = (|cnt_data) ?  10'b0 : ({data_10bx8[3][BWi-1], data_10bx8[3]} - {data_10bx8[4][BWi-1], data_10bx8[4]}); // 9
assign v5 = (|cnt_data) ?  10'b0 : ({data_10bx8[2][BWi-1], data_10bx8[2]} - {data_10bx8[5][BWi-1], data_10bx8[5]}); // 9
assign v6 = (|cnt_data) ?  10'b0 : ({data_10bx8[1][BWi-1], data_10bx8[1]} - {data_10bx8[6][BWi-1], data_10bx8[6]}); // 9
assign v7 = (|cnt_data) ?  10'b0 : ({data_10bx8[0][BWi-1], data_10bx8[0]} - {data_10bx8[7][BWi-1], data_10bx8[7]}); // 9

assign v8 = v0 + v3;
assign v9 = v1 + v2;
assign v10 = v1 - v2;
assign v11 = v0 - v3;
assign v12 = -v4 - v5;
assign vv13 = v5 + v6;
assign v13 = ((vv13 <<< 1) + vv13) >>> 2;
assign v14 = v6 + v7;

assign v15 = v8 + v9;
assign v16 = v8 - v9;
assign vv17 = v10 + v11;
assign vv18 = v12 + v14;
assign v17 = ((vv17 <<< 1) + vv17) >>> 2;
assign v18 = ((vv18 <<< 1) + vv18) >>> 3;

assign v19 = ((-v12) >>> 1) - v18;
assign v20 = (((v14 <<< 2) + v14) - (v18 <<< 2)) >>> 2;

assign v21 = v17 + v11;
assign v22 = v11 - v17;
assign v23 = v13 + v7; 
assign v24 = v7 - v13; 

assign v25 = v19 + v24;
assign v26 = v23 + v20;
assign v27 = v23 - v20;
assign v28 = v24 - v19;

assign out1 = v26 >>> 1;
assign out2 = v21 >>> 1;
assign out3 = ((v28 <<< 2) + v28) >>> 3;
assign out4 = ((v16 <<< 1) + v16) >>> 2;
assign out5 = ((v25 <<< 3) - v25) >>> 3;
assign out6 = (v22 + (v22 <<< 2)) >>> 2;
assign out7 = ((v27 <<< 2) + v27) >>> 1;

assign dct_out = data_outs[cnt_data_out];

assign tp_mem_enb = tp_enb_delayed;

always @ (posedge clk) begin
    if (rst) begin
        data_10bx8[0] <= 10'b0;
        data_10bx8[1] <= 10'b0;
        data_10bx8[2] <= 10'b0;
        data_10bx8[3] <= 10'b0;
        data_10bx8[4] <= 10'b0;
        data_10bx8[5] <= 10'b0;
        data_10bx8[6] <= 10'b0;
        data_10bx8[7] <= 10'b0;

        data_outs[0] <= 12'b0;
        data_outs[1] <= 12'b0;
        data_outs[2] <= 12'b0;
        data_outs[3] <= 12'b0;
        data_outs[4] <= 12'b0;
        data_outs[5] <= 12'b0;
        data_outs[6] <= 12'b0;
        data_outs[7] <= 12'b0;

        cnt_data <= 3'b0;
        cnt_data_out <= 3'b0;
        tp_enb <= 1'b0;
        tp_enb_delayed <= 1'b0;
    end
    else if (enb) begin
        if (cnt_data == 3'd7) begin
            cnt_data <= 3'b0;
            tp_enb <= 1'b1;
        end
        else if (cnt_data == 3'b0) begin
            data_outs[0] <=  v15[BWi+2 -: BWo];
            data_outs[1] <= {out1[BWi+3], out1[0 +: BWo - 1]};
            data_outs[2] <= {out2[BWi+3], out2[0 +: BWo - 1]};
            data_outs[3] <= {out3[BWi+3], out3[0 +: BWo - 1]};
            data_outs[4] <= {out4[BWi+3], out4[0 +: BWo - 1]};
            data_outs[5] <= {out5[BWi+3], out5[0 +: BWo - 1]};
            data_outs[6] <= {out6[BWi+3], out6[0 +: BWo - 1]};
            data_outs[7] <= {out7[BWi+3], out7[0 +: BWo - 1]};

            cnt_data <= cnt_data + 3'b1;
        end
        else begin
            cnt_data <= cnt_data + 3'b1;
        end
        
        cnt_data_out <= cnt_data;
        tp_enb_delayed <= tp_enb;

        data_10bx8[cnt_data] <= dct_in;
    end
end

endmodule
