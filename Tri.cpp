#include<bits/stdc++.h>
using namespace std;
int main(){
    int a[3];
    for(int i=0;i<3;i++){
        cin>>a[i];
    }
    for(int i=0;i<1;i++){
    if(a[0]==a[1]+a[2]){
        cout<<a[0]<<"="<<a[1]<<"+"<<a[2];
        break;
    }
    if(a[0]==a[1]-a[2]){
        cout<<a[0]<<"="<<a[1]<<"-"<<a[2];
        break;
    }
    if(a[0]==a[1]*a[2]){
        cout<<a[0]<<"="<<a[1]<<"*"<<a[2];
        break;
    }
    if(a[0]==a[1]/a[2]){
        cout<<a[0]<<"="<<a[1]<<"/"<<a[2];
        break;
    }
    
    
    if(a[0]+a[1]==a[2]){
        cout<<a[0]<<"+"<<a[1]<<"="<<a[2];
        break;
    }
    if(a[0]-a[1]==a[2]){
        cout<<a[0]<<"-"<<a[1]<<"="<<a[2];
        break;
    }
    if(a[0]*a[1]==a[2]){
        cout<<a[0]<<"*"<<a[1]<<"="<<a[2];
        break;
    }
    if(a[0]/a[1]==a[2]){
        cout<<a[0]<<"/"<<a[1]<<"="<<a[2];
        break;
    }
        
    }}