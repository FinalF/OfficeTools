#include <unistd.h>
#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>
#include <stdlib.h>

void pullFileFromDir(char *sourcedir, char *destidir)
{
	DIR *dp;
	char cpy_cmd[300];
	char rootpath[150];
	char dirpath[300];
	struct dirent *entry;
	struct stat statbuf;
	if((dp = opendir(sourcedir)) == NULL) {
		fprintf(stderr,"cannot open directory: %s\n", sourcedir);
		return;
	}
	chdir(sourcedir);
	
	while((entry = readdir(dp)) != NULL) {
		memset(dirpath, 0, sizeof(dirpath));
		strcpy(dirpath, sourcedir);
		strcat(dirpath, "/");
		strcat(dirpath, entry->d_name);
//		printf("subdir: %s\n", dirpath);
		lstat(dirpath,&statbuf);
		if(S_ISDIR(statbuf.st_mode)) {
			if(strcmp(entry->d_name, ".") && strcmp(entry->d_name, ".."))
			/*find the directory, enter it*/
			pullFileFromDir(dirpath, destidir);

		}
		else{// printf("%*s%s\n",depth,"",entry->d_name);
//printf("file: %s\n", entry->d_name);
			sprintf(cpy_cmd, "cp ./%s %s", entry->d_name, destidir);	
//			printf("%s\n", cpy_cmd);
			system(cpy_cmd); 
		}
	}
		chdir("..");
		closedir(dp);

}



int main(int argc, char* argv[]){
	 char *topdir = ".";
	 char *desdir = NULL;
	 
	 if (argc == 3){
		 topdir=argv[1];
		 desdir=argv[2];
	 }else{
		 printf("Please input the source directory and destination directory");
	 }
	 
	 printf("Directory scan of %s\n",topdir);
	 pullFileFromDir(topdir,desdir);
	 printf("done.\n");
	 exit(0);
 }

