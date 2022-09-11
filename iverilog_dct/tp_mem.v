module tp_mem
#(parameter BW = 8)
(
    output [BW-1:0] mem_out,
    output reg enb_out,
    input  [BW-1:0] mem_in,
    input  clk, rst, enb
);

reg [BW-1:0] data [0:7][0:7];
reg odd;
reg [2:0] cnt_row, cnt_col;

assign mem_out = odd ? data[cnt_row][cnt_col] : data[cnt_col][cnt_row];

always @ (posedge clk) begin
    if (rst) begin
        odd        <= 1'b0;
        cnt_row    <= 3'b0;
        cnt_col    <= 3'b0;
        enb_out    <= 1'b0;
    end
    else if (enb) begin
        if (cnt_col == 3'd7) begin
            cnt_col <= 3'b0;
            if (cnt_row == 3'd7) begin
                cnt_row <= 3'b0;
                enb_out <= 1'b1;
                odd <= ~odd;
            end
            else begin
                cnt_row <= cnt_row + 3'b1;
            end
        end
        else begin
            cnt_col <= cnt_col + 3'b1;
        end
    end
end

always @ (posedge clk) begin
    if (rst) begin
        data[0][0] <= 0;
        data[1][0] <= 0;
        data[2][0] <= 0;
        data[3][0] <= 0;
        data[4][0] <= 0;
        data[5][0] <= 0;
        data[6][0] <= 0;
        data[7][0] <= 0;
        data[0][1] <= 0;
        data[1][1] <= 0;
        data[2][1] <= 0;
        data[3][1] <= 0;
        data[4][1] <= 0;
        data[5][1] <= 0;
        data[6][1] <= 0;
        data[7][1] <= 0;
        data[0][2] <= 0;
        data[1][2] <= 0;
        data[2][2] <= 0;
        data[3][2] <= 0;
        data[4][2] <= 0;
        data[5][2] <= 0;
        data[6][2] <= 0;
        data[7][2] <= 0;
        data[0][3] <= 0;
        data[1][3] <= 0;
        data[2][3] <= 0;
        data[3][3] <= 0;
        data[4][3] <= 0;
        data[5][3] <= 0;
        data[6][3] <= 0;
        data[7][3] <= 0;
        data[0][4] <= 0;
        data[1][4] <= 0;
        data[2][4] <= 0;
        data[3][4] <= 0;
        data[4][4] <= 0;
        data[5][4] <= 0;
        data[6][4] <= 0;
        data[7][4] <= 0;
        data[0][5] <= 0;
        data[1][5] <= 0;
        data[2][5] <= 0;
        data[3][5] <= 0;
        data[4][5] <= 0;
        data[5][5] <= 0;
        data[6][5] <= 0;
        data[7][5] <= 0;
        data[0][6] <= 0;
        data[1][6] <= 0;
        data[2][6] <= 0;
        data[3][6] <= 0;
        data[4][6] <= 0;
        data[5][6] <= 0;
        data[6][6] <= 0;
        data[7][6] <= 0;
        data[0][7] <= 0;
        data[1][7] <= 0;
        data[2][7] <= 0;
        data[3][7] <= 0;
        data[4][7] <= 0;
        data[5][7] <= 0;
        data[6][7] <= 0;
        data[7][7] <= 0;
        // data[0][8] <= 8'b0;
        // data[1][8] <= 8'b0;
        // data[2][8] <= 8'b0;
        // data[3][8] <= 8'b0;
        // data[4][8] <= 8'b0;
        // data[5][8] <= 8'b0;
        // data[6][8] <= 8'b0;
        // data[7][8] <= 8'b0;
        // data[8][8] <= 8'b0;
    end
    else if (odd) begin
        data[cnt_row][cnt_col] <= mem_in;
    end
    else begin
        data[cnt_col][cnt_row] <= mem_in;
    end
end

endmodule
