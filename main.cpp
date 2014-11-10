#include <iostream>
#include <fstream>
#include <string>
#include <iterator>

void replaceTableWithReponsive(std::string &fileContents, std::string const &fileName);

int main(){
  std::string fileName = "GoodrichTamassiaGoldwasserPages.html";
  std::ifstream infile(fileName);
   if ( infile ) {
      std::string fileData( ( std::istreambuf_iterator<char> ( infile ) ) ,
	    std::istreambuf_iterator<char> ( ) ) ;
      infile.close( ) ; ;
      replaceTableWithReponsive(fileData, fileName);

   }
   else {
      std::cout << "file not found!\n" ;
      return 1 ;
   }
   
   return 0 ;
}

void replaceTableWithReponsive(std::string &fileContents, std::string const &fileName) {
  size_t pos = 0;
  std::string findStr = R"(<table)";
  std::string insertStr = R"(<div class="table-responsive">)";
  while ((pos = fileContents.find(findStr, pos)) != std::string::npos) {
    fileContents.insert(pos, insertStr);
    pos += insertStr.length() + findStr.length();
  }
  pos = 0;
  findStr = R"(</table>)";
  insertStr = R"(</div>)";
  while ((pos = fileContents.find(findStr, pos)) != std::string::npos) {
    pos = pos + findStr.length();
    fileContents.insert(pos, insertStr);
    pos += insertStr.length();
  }

  std::ofstream out(fileName);
  std::copy(fileContents.begin(), fileContents.end(), std::ostreambuf_iterator<char>(out));
}