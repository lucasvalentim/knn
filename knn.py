import numpy as np


class KNN(object):
    def __init__(self, k, metrica='euclidiana'):
        self.k = k
        self.metrica = metrica

    def distancia(self, ponto_a, ponto_b):
        somatorio = 0
        
        if self.metrica == 'manhattan':
            for i in range(len(ponto_a)):
                somatorio += abs(ponto_b[i] - ponto_a[i])
            
            return somatorio
                
        elif self.metrica == 'euclidiana':
            for i in range(len(ponto_a)):
                somatorio += (ponto_b[i] - ponto_a[i]) ** 2
            
            return somatorio ** 0.5 
    
    def ordenar_vizinhos(self):
        self.vizinhos = sorted(self.vizinhos, key=lambda vizinho: vizinho[0])
    
    def treinar(self, X, y):
        self.X = X
        self.y = y
        
    def classificar(self, x):
        self.vizinhos = []
        
        for i in range(len(self.X)):
            self.vizinhos.append((self.distancia(x, self.X[i]), self.y[i]))
            
        self.ordenar_vizinhos()
        
        y_ocorrencias = {}
        
        for i in range(self.k):
            if self.vizinhos[i][1] in y_ocorrencias:
                y_ocorrencias[self.vizinhos[i][1]] += 1
            
            else:
                y_ocorrencias[self.vizinhos[i][1]] = 1
        
        y_mais_ocorrente = None
        
        for y in y_ocorrencias:
            if y_mais_ocorrente == None or y_ocorrencias[y] > y_ocorrencias[y_mais_ocorrente]:
                y_mais_ocorrente = y

        return y_mais_ocorrente