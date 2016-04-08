import sys

sys.path.insert(0, '../libs')

import clusters

blognames,words,data=clusters.readfile('blogdata1.txt')
clust = clusters.hcluster(data)

# print ASCII dendrogram
clusters.printclust(clust, labels=blognames)

# save JPEG dendrogram
clusters.drawdendrogram(clust, blognames, jpeg='blogclust.jpg')

