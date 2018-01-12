//
//  HashTable.cpp
//  
//
//  Created by phillip zachariah on 1/10/18.
//
//

#include <vector>
#include <string>
#include <iostream>
#include <math.h>
using namespace std;

struct node{
    node* prev;
    node* next;
    string value;
    int key;
};
class HashTable{
    
    vector<node*> HashTable;
    int TableSize;
    public:
        void    init_HashTable(int sizeofTable);
        void    insertion(string x);
        bool  search(string x);
        void    deletion(string x);
        int     HashFunc(string words);
        void    sizeofHashTable();
        node*    endOfList(int x);
    
    
};
void HashTable::init_HashTable(int sizeofTable)
{
    vector<node*> defaultHashtable(sizeofTable);
    for(int i =0;i <sizeofTable; i++)
    {
        defaultHashtable.at(i) = NULL;
    }
    this->TableSize = sizeofTable;
    this->HashTable = defaultHashtable;
    
}
node* HashTable::endOfList(int x)
{
    if(HashTable.at(x) == NULL)
    {
        return NULL;
    }
    else{
            node* currnode = HashTable.at(x);
        
            while(currnode->next!= NULL)
            {
                cout << "moving over" << endl;
                currnode = currnode->next;
            }
          // cout <<"last node: " <<  currnode << endl;
           // cout << "went here" << endl;
            return currnode;
    }

    
}
//This initializes your Hashtable to the certain size it desires.
void HashTable::insertion(string x)
{
    int key = HashFunc(x);
    //This creates a new node with the current name and its key
     node* newnode = new node;
     newnode->value = x;
    newnode->key  = key;
    newnode->next = NULL;
    node* lastnode = this->endOfList(key);
    //if the last node is null, that means that the linked list of that key is empty, therefore we can just go ahead and add it
    if(lastnode == NULL){
        cout << "first one of this key " << endl << endl ;
        newnode->prev = NULL;
        HashTable.at(key) = newnode;
    }
    else{ // the linked list already had a key/value pair so therefore a collision occured.
        cout << "collision" << endl << endl;
            node* prevnode  = lastnode;
            newnode->prev    = prevnode;
            prevnode->next  = newnode;
          //  cout << "newnode address: " << &newnode << endl;
    }
}
bool HashTable::search(string x)
{
    bool flag = false;
    int key = HashFunc(x);
    node* currlist = HashTable.at(key);
    if(currlist == NULL)
    {
        //do nothing first that means there is nothing in the current linked list at key location.
    }
    else{
        //there is already one name inside the loop so therefore we need to determine if  it is actually inside the linked list now.
        while(currlist->next != NULL){
            if(currlist->value == x)
            {
                flag = true;
            }
            
            currlist = currlist->next;
        }

    }
    if(flag == false)
    {
        cout << x << " was" << " not found inside loop " << endl;
    }
    else{
        cout << x << " was" << " found inside loop " << endl;
    }
    return flag;
    
    
}
void HashTable::deletion(string x)
{
    
}
void HashTable::sizeofHashTable()
{
    cout << "SIZE OF HASHTABLE : " << this->HashTable.size() << endl;
}
// HASH FUNCTION WAS TAKEN FROM : https://stackoverflow.com/questions/8317508/hash-function-for-a-string
//M is gonna be the size of the table.
int HashTable::HashFunc(string word)
{
    int seed = 131;
    unsigned long hash = 0;
    for(int i = 0; i < word.length(); i++)
    {
        hash = (hash * seed) + word[i];
    }
    return hash % this->TableSize;
}


int main()
{
    HashTable x;
    node test;
    
    test.value = "phillip";
    x.init_HashTable(10);
    x.sizeofHashTable();
    x.insertion(test.value);
    x.insertion(test.value);
    x.insertion(test.value);
    x.insertion(test.value);
     test.value = "Nathan";
    x.search(test.value);
     x.search("phillip");
    x.insertion(test.value);
    x.insertion(test.value);
    x.insertion(test.value);
    x.insertion(test.value);
   // x.search(test.value);


    
    
    
    
    
    
    
    
    
    
    
    
    
}
