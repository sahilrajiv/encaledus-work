





strecker_syn_part1 = ruleGMLString("""rule [
    ruleID "Strecker Synthesis Part 1"
    labelType "term"
    left [
       
     
        
     edge [ source 2 target 3 label "=" ]
     
      
       
 
        edge [ source 9 target 10 label "-" ]
    ]
    context [
        node [ id 1 label "*" ]
        node [ id 2 label "C" ]
        node [ id 3 label "O" ]
         node [ id 4 label "*" ]
       
          
      
          
            edge [ source 1 target 2 label "-" ]
        edge [ source 4 target 2 label "-" ]
       
       
          
          
          
          # part 2
        node [ id 9 label "H" ]
        node [ id 10 label "C" ]
        node [ id 11 label "N" ]
         
        edge [ source 10 target 11 label "#" ]
         
        

        
       
     
        
    ]
    right [
      
     
        edge [ source 2 target 3 label "-" ]
        
        edge [ source 10 target 2 label "-" ]
           edge [ source 3 target 9 label "-" ]
    ]
    constrainAdj [
        id 2 op "=" count 0
        nodeLabels [ label "O" label "N" label "S" ]
        edgeLabels [ label "-" ]
    ]
    constrainAdj [
        id 5 op "=" count 0
        nodeLabels [ label "O" label "S" ]
        edgeLabels [ label "-" ]
    ]
    constrainAdj [
        id 6 op "=" count 0
        nodeLabels [ label "O" label "S" ]
        edgeLabels [ label "=" ]
    ]
    constrainAdj [
        id 7 op "=" count 0
        nodeLabels [ label "O" label "S" ]
        edgeLabels [ label "=" ]
    ]
]""")


strecker_syn_part2 = ruleGMLString("""rule [
    ruleID "Strecker Synthesis Part 2"
    labelType "term"
    left [
            edge [ source 2 target 3 label "-" ]
        
        edge [ source 10 target 2 label "-" ]
           edge [ source 3 target 9 label "-" ]
      
        edge [ source 5 target 8 label "-" ]
        
    ]
    context [
        node [ id 1 label "*" ]
        node [ id 2 label "C" ]
        node [ id 3 label "O" ]
         node [ id 4 label "*" ]
        node [ id 5 label "N" ]
        node [ id 6 label "*" ]
        node [ id 7 label "*" ]
          node [ id 8 label "H" ]
          
          
             
          # part 2
        node [ id 9 label "H" ]
        node [ id 10 label "C" ]
        node [ id 11 label "N" ]
         
        edge [ source 10 target 11 label "#" ]
         
  
        edge [ source 1 target 2 label "-" ]
        edge [ source 4 target 2 label "-" ]
        edge [ source 6 target 5 label "-" ] 
        edge [ source 7 target 5 label "-" ]      
    ]
    right [
    
    
    
        edge [ source 2 target 5 label "-" ]
          edge [ source 2 target 10 label "-" ] 
 
       
        edge [ source 3 target 8 label "-" ]
             edge [ source 3 target 9 label "-" ]
     
      
    ]
    constrainAdj [
        id 2 op "=" count 0
        nodeLabels [ label "O" label "N" label "S" ]
        edgeLabels [ label "-" ]
    ]
    constrainAdj [
        id 5 op "=" count 0
        nodeLabels [ label "O" label "S" ]
        edgeLabels [ label "-" ]
    ]
    constrainAdj [
        id 6 op "=" count 0
        nodeLabels [ label "O" label "S" ]
        edgeLabels [ label "=" ]
    ]
    constrainAdj [
        id 7 op "=" count 0
        nodeLabels [ label "O" label "S" ]
        edgeLabels [ label "=" ]
    ]
]""")


