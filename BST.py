"""
Aurelio Amparo
Binary Search Tree
"""


# its a node function
class Node:
    def __init__(self,ID, val, left=None, right=None):
        self.ID = ID
        self.data = val
        self.left = left
        self.right = right
    
class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    #if root exist calls our _put function
    #else makes our node the root and also adds to size
    def put(self,node):
        if self.root != None:
            self._put(self.root,node)
        else:
            self.size +=1
            self.root = node


    def _put(self,root,node):
        #if our current root id > than node's id
        #assigns our node to root.left
        if root.ID > node.ID:
            if root.left == None:
                self.size +=1
                root.left = node
            else:
                self._put(root.left,node)
        #assigns our node to root.right
        elif root.ID < node.ID:
            if root.right == None:
                self.size +=1
                root.right = node
            else:
                self._put(root.right,node)
        else:
            print("Value already exists!")
    
    def searchTree(self,ID):
        if self.root == None:
            return 0        
        #if the root of the node == to our ID we are looking for returns node data
        elif self.root.ID == ID:
            return self.root.data

        else:
        # else, uses our search tree function
            return self._searchTree(self.root,ID)
    # TODO function optimize
    def _searchTree(self,root,ID):
        
        if root.ID  > ID:
            if root.left != None:
                #uses root.left and our ID (userInput) to recurse until employee is found
                return self._searchTree(root.left,ID)
                
        elif root.ID < ID:
            if root.right != None:
                #uses root.right and our ID (userInput) to recurse until employee is found
                return self._searchTree(root.right,ID)
        #if our root.ID matches our ID(userInput) we return that node
        else:
            return root
    def printTree(self,root):
        if root.left:
            self.printTree(root.left)
            print("left: "+root.left.ID)
        if root.right:
            self.printTree(root.right)
            print(root.right.ID)

def Main():
    tree = BST()
    file = open("EmployeeList.csv")
    for line in file.read().split("\n"):
        line = line.split(",")
        n = Node(ID = line[0],val = line[1:])
        tree.put(n)
    while True:
        userInput = input("Enter ID Number (Q) to Quit: ").upper()
        if userInput == "Q":
            break
        result = tree.searchTree(userInput)
        if result:
            header = ["FirstName: ","LastName: ","Phone: ","SSN: ","Address: ","Rank: ","Salary: $"]
            print("Employee found!")
            for i in range(len(result.data)): 
                print(header[i]+result.data[i])
            
        else:
            print("Employee not found")
    tree.printTree(tree.root)
Main()