#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// int main(void)
// {
//  char url[]="ITENS_PROVA_2019.csv";
//  char ch;
//  int x;
//  FILE *arq;
//  int tt = 1;
//  srand( (unsigned)time(NULL) );
//  arq = fopen(url, "r");
//  if(arq == NULL)
//      printf("Erro, nao foi possivel abrir o arquivo\n");
//  else
//     //  while( (ch=fgetc(arq))!= EOF ){
//     //     // x = rand() % 52;
//     //     // if(tt == 1){
//     //     //     putchar(ch);
//     //     //     tt = 0;
//     //     // }
//     //     // else if(x>50){
//     //     //     putchar(ch);
//     //     // }
//     //     putchar(ch);
//     //  }
   
//  fclose(arq);
 
//  return 0;
// }


int main(void)
{
    FILE * fp;
    FILE * save;
    char * line = NULL;
    size_t len = 0;
    size_t read;
    int tt = 1;
    int x;
    int count = 0;
    srand( (unsigned)time(NULL) );
    fp = fopen("ENEM_data_for_modeling.csv", "r");
    save = fopen("0.05_ENEM_data_for_modeling.csv","w");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        //printf("Retrieved line of length %zu:\n", read);
        x = rand()%100;
        if(tt==1){
            fprintf(save,"%s", line);
            tt = 0;
        }
        if (x>=97){
            fprintf(save,"%s", line);
            count++;
        }
    }
    printf("%d",count);
    fclose(fp);
    fclose(save);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}