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

integer i, j;    
    
always @ (posedge clk) begin
    if (rst) begin
        for (i=0;i<8;i=i+1) begin
            for (j=0;j<8;j=j+1) begin
                data[j][i] <= 0;
            end
        end
    end
    else if (odd) begin
        data[cnt_row][cnt_col] <= mem_in;
    end
    else begin
        data[cnt_col][cnt_row] <= mem_in;
    end
end

endmodule
