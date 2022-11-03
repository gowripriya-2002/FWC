module helloworldfpga(                    
    input  wire U,
    input  wire V,
    input  wire Z,
    input  wire W,
    output wire F,                   
    );                                     
    assign U=0;                               
    assign V=0;
    assign Z=1;
    assign W=1;
 
  always @(*)                         
  begin
  F=((U&!Z)|(!V&Z)|(!U&Z&!W));             
  end                                     
  endmodule
