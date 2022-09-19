#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b;
    cin>>a>>b;
    int c[b];
    for(int i=0;i<b;i++){
        cin>>c[i];
    }
    int sum=0;
    for(int i=0;i<b;i++){
        sum=sum+(a-c[i]);
    }
    cout<<sum+a;
    
}