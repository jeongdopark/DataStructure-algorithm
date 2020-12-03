class Node{
    constructor(element){
        this.element = element;
        this.next = null;
        this.previous = null;        
    }
}

class LList{
    constructor(){
        this.head = new Node("head");
    }

    find(item){
        let currentNode = this.head;
        while(currentNode.element != item){
            currentNode = currentNode.next;
        }
        return currentNode
    }

    insert(newItem, item){
        const newNode = new Node(newItem);
        const currentNode = this.find(item);  
                 
        if(currentNode.next != null){
            newNode.next = currentNode.next;
            currentNode.next = newNode;
            newNode.next.previous = newNode;
            newNode.previous = currentNode;

        }else if(currentNode.next == null){
            newNode.next = currentNode.next;
            currentNode.next = newNode;
            newNode.previous = currentNode;
        }
        
    }

    beforeNode(item){
        let currentNode = this.head;
        while(currentNode.next.element != item){
            currentNode = currentNode.next;
        }
        return currentNode;
    }

    

    remove(removeItem){
        const removeThisNode = this.find(removeItem);
        if(!(removeItem.next == null)){
            removeThisNode.previous.next = removeThisNode.next;
            removeThisNode.next.previous = removeThisNode.previous;
            removeThisNode.previous = null;
            removeThisNode.next = null;
        }else{
            removeThisNode.previous = null;
            removeThisNode.previous.next = removeThisNode.next;
        }
        
    }

    display(){
        let displayElement = [];
        let start = this.head.next;
        while(start != null){                       
            displayElement.push(start.element);
            start = start.next;
            
        }
        return displayElement;
    }

    displayReverse(){
        let nodeArray = [];
        let lastNode = this.findLastNode();
        while(lastNode.previous != null){
            nodeArray.push(lastNode.element);
            lastNode = lastNode.previous;
        }
        return nodeArray;
    }

    findLastNode(){
        let searchNode = this.head;
        while(searchNode.next != null){
            searchNode = searchNode.next;
        }
        return searchNode;
    }
}






























