import math as j
class Node:
    def __init__(self, state, parent, actions,cost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.cost = cost


graph = {'A': Node('A', None, [('B',6),('C',9),('E',1)], 0),
         'B': Node('B', None, [('A',6),('D',3),('E',4)], 0),
         'C': Node('C', None, [('A',9),('F',2),('G',3)], 0),
         'D': Node('D', None, [('B',3), ('E',5), ('F',7)], 0),
         'E': Node('E', None, [('A',1), ('B',4), ('D',5)], 0),
         'F': Node('F', None, [('C',2),('D',6),('E',7)], 0),
         'G': Node('G', None, [('C',3)], 0)
        }

def findMin(front):
    minV=j.inf
    node = ''
    for i in front:
        if minV>front[i][1]:
            minV=front[i][1]
            node=i
    return node

def UCS(graph, initial, goal):
    front=dict()
    front[initial]=(None,0)
    explored=[]

    while len(front)!=0:
        cNode=findMin(front)
        del front[cNode]
        if graph[cNode].state ==  goal:
            return action_seqe(graph, initial, goal)
        explored.append(cNode)
        for child in graph[cNode].actions:
            cCost = child[1] + graph[cNode].cost
            if child[0] not in front and child[0] not in explored:
                graph[child[0]].parent = cNode
                graph[child[0]].cost = cCost
                front[child[0]] = (graph[child[0]].parent, graph[child[0]].cost)
            elif child[0] in front:
                if front[child[0]][1] < cCost:
                    graph[child[0]].parent = front[child[0]][0]
                    graph[child[0]].cost = front[child[0]][1]
                else:
                    front[child[0]] = (cNode,cCost)
                    graph[child[0]].parent = front[child[0]][0]
                    graph[child[0]].cost = front[child[0]][1]

def action_seqe(graph, initial, goal):
    solution=[goal]
    c_parent=graph[goal].parent
    while c_parent != None:
        solution.append(c_parent)
        c_parent = graph[c_parent].parent
    solution.reverse()
    return solution


initialstate = input('Enter Initial State: ')
goalstate = input('Enter Goal State: ')

if(initialstate.capitalize() in graph.keys()):
    if(goalstate.capitalize() in graph.keys()):
        solution = UCS(graph, initialstate.capitalize(), goalstate.capitalize())
        for i in solution:
            print(i , end='')
            if i != solution[-1]:
                print(" -> ", end='')
    else:
        print('Wrong Goal State')
else:
    print('Wrong Initial State')