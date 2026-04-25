`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2026/04/24 23:40:17
// Design Name: 
// Module Name: sqrt
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


module sqrt(num, sqrt_num);
    input [3:0] num;
    output [2:0] sqrt_num;
    //中间量
    wire not_a, not_b, not_c, not_d, c_or_d, not_x,
        y1, y2, y3, y4,
        t1, t2, t3, t4, t5, t6, t7, c_xor_d;
    //X计算
    not not1(not_c, num[1]);
    not not2(not_d, num[0]);
    nand na1(c_or_d, not_c, not_d);
    nand na2(not_x, num[3], num[2], c_or_d);
    not not3(sqrt_num[2], not_x);
    //Y计算
    //部分1
    not not4(not_b, num[2]);
    nand na3(y1, not_b, num[3]);
    //部分2
    not not5(not_a, num[3]);
    nand na4(y2, not_a, num[2]);
    //部分3
    nand na5(y3, not_a, num[1], num[0]);
    //部分4
    nand na6(y4, num[3], not_c, not_d);
    //合并
    nand na7(sqrt_num[1], y1, y2, y3, y4);
    //Z计算
    //部分1
    nand na8(t1, not_c, not_d);
    nand na9(t2, t1, num[2]);
    nand na10(t3, t2, num[3]);
    //部分2
    nand na11(t4, not_d, num[1]);
    nand na12(t5, not_c, num[0]);
    nand na13(c_xor_d, t4, t5);
    nand na14(t6, c_xor_d, not_b);
    //部分3
    nand na15(t7, not_a, num[2], num[1], num[0]);
    //NAND合并
    nand na16(sqrt_num[0], t3, t6, t7);
    
endmodule