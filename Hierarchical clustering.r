#Hierarchical clustering

# Importing the mall dataset
dataset = read.csv(‘mall.csv’)
X = dataset[4:5]

#Using the dendrogram to find optimal number of clusters
dendrogram<-hclust(dist(X, method = "euclidean"), method = "ward.D")
plot(dendrogram,
main = paste('Dendrogram'),
xlab= 'Customers',
ylab= 'Euclidean Distance')

#Fitting hierarchical clustering to the mall dataset
hc<-hclust(dist(X, method = "euclidean"), method = "ward.D")
y_hc= cutree(hc, 5)

# Visualizing the cluster
library(cluster)
clusplot(X,
y_hc,
lines = 0,
shade = TRUE,
color = TRUE,
labels = 2,
plotchar= FALSE,
span = TRUE,
main = paste(‘Cluster of clients'),
xlab= “Annual income",
ylab= “Spending score")