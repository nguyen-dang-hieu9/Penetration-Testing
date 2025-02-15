#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int a = 0;
	char path[100] = "/tmp/ahihi.txt"; 
	char buffer[100];
	char method[5];
	FILE *f;

	strcpy(method,getenv("REQUEST_METHOD"));
	if (strcmp(method,"GET")==0){
		strcpy(buffer, getenv("QUERY_STRING"));
	}
	else if(strcmp(method,"POST")==0){
		scanf("%s",buffer);
	}
	else{

		printf("Content-type: text/html\n\nUnsupported method\n\r");
		return 0;
	}


	
	f = fopen(path,"a+");
	fprintf(f,"%s: %s ---- %s",getenv("REMOTE_ADDR"), method, buffer);
	fclose(f);


	printf("Content-type: text/html\n\n[%s] %s\n\r",path,buffer);
	return 0;
}
