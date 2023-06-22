beta_e = """rule [
	ruleID "Fe3 Complex Beta elimination from a sugar and Conversion to Acid"
	left[


                edge[ source 9 target 10 label "-"]

                edge[ source 5 target 4 label "-"]
                edge[ source 1 target 2 label "-"]


	]
	context [
	        node [id 1 label "C"]
                node [id 2 label "H"]
                
                node [id 3 label "O"]
                 node [id 4 label "H"]               
                node [id 5 label "C"]
                node [id 6 label "O"]
                node [id 7 label "H"]
                node [id 8 label "Fe3+"]
        
        
                node [id 9 label "C"]

                node [id 10 label "O"]
                node [id 11 label "H"]
                node [id 12 label "H"]
                node [id 13 label "*"] #change to * later
        

                              edge[ source 1 target 3 label "="]
                
                
                # edge[ source 3 target 8 label "-"]
                # edge[ source 8 target 6 label "-"]
                edge[ source 6 target 7 label "-"]
                edge[ source 6 target 5 label "-"]
                edge[ source 9 target 12 label "-"]
                edge[ source 9 target 13 label "-"]
                edge[ source 10 target 11 label "-"]
                edge[ source 9 target 5 label "-"]

                edge[ source 1 target 5 label "-"]
                
       
	]


	right [
                
                
                
                
                edge[ source 1 target 10 label "-"]
                
                edge[ source 9 target 4 label "-"]
                edge[ source 5 target 2 label "-"]

        	
	]
	
]
"""


beta_el= ruleGMLString(beta_e)
p=GraphPrinter()
# beta_el.print()


