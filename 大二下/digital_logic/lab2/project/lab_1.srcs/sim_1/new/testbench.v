`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2026/04/25 00:57:34
// Design Name: 
// Module Name: testbench
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module testbench(
    );
    reg [3:0] in;
    wire [2:0] out;

    sqrt sqrt_test(
        .num(in),
        .sqrt_num(out)
    );

    initial begin
       //测试0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
        in <= 4'd0;
        #20 in<= 4'd1 ;
        #20 in<= 4'd2 ;
        #20 in<= 4'd3 ;
        #20 in<= 4'd4 ;
        #20 in<= 4'd5 ;
        #20 in<= 4'd6 ;
        #20 in<= 4'd7 ;
        #20 in<= 4'd8 ;
        #20 in<= 4'd9 ;
        #20 in<= 4'd10 ;
        #20 in<= 4'd11 ;
        #20 in<= 4'd12 ;
        #20 in<= 4'd13 ;
        #20 in<= 4'd14 ;
        #20 in<= 4'd15 ;
        #20 $finish;
    end
endmodule
