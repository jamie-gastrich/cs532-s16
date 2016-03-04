library("igraph") # loads the packages needed
g <- read.graph("karate.gml", format="gml") # I found this .gml file from http://networkdata.ics.uci.edu/data/karate/karate.gml and https://github.com/maturban/cs595-f13/tree/master/assignment6
print('Edges will be deleted in the following order : ') # prints a friendly message allowing the user to knwo what is about to happen
repeat{
	edges_betweenness <- edge.betweenness(g)	#Computes the betweeness of the edges																								#
	max_value <- max(edges_betweenness)																											# 
	edge_to_delete <- match(c(max_value),edges_betweenness)			# deletes the edges as it goes along																			#
	print(paste(paste(paste(get.edgelist(g)[edge_to_delete,1]," -> "),get.edgelist(g)[edge_to_delete,2]),paste("  -- Betweenness = ",max_value)))# This is the algorithm of the 
	g <- delete.edges(g, E(g, P=c(get.edgelist(g)[edge_to_delete,1],get.edgelist(g)[edge_to_delete,2])))										# scenario of the Karate club
	cluster_no <- clusters(g)['no']																												#
	if(cluster_no == 2)
	#From this point on it sets up the graph with specific attributes
	{
		break
	}
	cs <- leading.eigenvector.community(g, steps=1)
	V(g)$color <- ifelse(cs$membership==1, "white", "red")
	scale <- function(v, a, b) {
  	v <- v-min(v) ; v <- v/max(v) ; v <- v * (b-a) ; v+a
	}
	E(g)$color <- "grey"
	E(g)[ V(g)[ color=="white" ] %--% V(g)[ color=="red" ] ]$color <- "red"
	tkplot(g, layout=layout.kamada.kawai, vertex.label.font=2)
}
cs <- leading.eigenvector.community(g, steps=1)
V(g)$color <- ifelse(cs$membership==1, "white", "red")
scale <- function(v, a, b) {
v <- v-min(v) ; v <- v/max(v) ; v <- v * (b-a) ; v+a
}
V(g)$size <- scale(abs(cs$eigenvectors[[1]]), 10, 20)
E(g)$color <- "grey"
E(g)[ V(g)[ color=="white" ] %--% V(g)[ color=="red" ] ]$color <- "red"
tkplot(g, layout=layout.kamada.kawai, vertex.label.font=2)