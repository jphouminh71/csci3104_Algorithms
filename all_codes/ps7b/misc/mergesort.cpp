#include <iostream>
using namespace std;

/*
  This function gets passed the sorted
*/
void merge(int* a, int s, int e){
  int mid = (s+e)/2;    // integer division, always rounds down

  int i = s;            // start of the index of the left array.
  int j = mid + 1;      // start of the index for the right side of the array
  int k = s;        // counter for the index of the array we are going to put together

  int temp[100];

  while ( i <= mid && j <= e ){
    // start putting elements into the array based on size
    if (a[i] < a[j]){
      temp[k++] = a[i++];
    }
    else{
      temp[k++] = a[j++];
    }
  }
  // now we fill the rest of the array with whichever sub-array isnt exhausted
  while( i <= mid){
    temp[k++] = a[i++];
  }
  while( j <= e ){
    temp[k++] = a[j++];
  }
  // copy all elements from the temporary array to the original array.

  for(int i =0; i <= e; i++){
    a[i] = temp[i];
  }

}

void mergesort(int a[],int s, int e){   // function takes in the array, the startIndex, and the endIndex, going to recursively call itself
  // base case, when either the sub-array size is 0 or 1
  if (s >= e){  // if the start index is equal to thend index or goes past the end index
    return ;
  }
  // recursively call the arrays , s->mid and mid+1,e
  int mid = (s+e)/2 ;     // automatically integer division, so it will always round down thats why we separate the left and right half by mid+1
  mergesort(a,s,mid);   // left half
  mergesort(a,mid+1,e); // right half
  // if we come down to this line it means that we have finished splitting and are going to begin merging all parts
  merge(a,s,e);
}


int main(int argc, char* argv[]){
  int a[100];   // this is the array we will be sorting.
  int n;        // this is for the end of our indexing array
  cin >> n;   // this is the size for our array

  for(int i = 0; i < n; i++){
    cin >> a[i];            // inputting actual elements
  }

  mergesort(a,0,n-1);     // mergesort all the shit in our array
  for(int i = 0; i < n; i++){
    cout << a[i] << ", ";
  }
  cout << endl;
  return 0;

}
