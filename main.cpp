#include <iostream>
#include <fstream>
#include <string>
#include <iterator>
#include <memory>

/*! @brief Code to make a collapsable chapter in the TableOfContents */
struct tocElement {
  std::string globalHeaderBegin = R"(<div class="panel-group" id="accordionToc">)";
  std::string globalHeaderEnd = R"(</div>)";
  /// @brief the preamble, replace the markup {{}} elements. 
  /// idx with a unique number
  /// headerMarkup with the previous header markup
  std::string header = R"(
  <div class="panel panel-default">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordionToc" href="#collapseToc{{idx}}">
<span class="pull-right clickable"><i class="glyphicon glyphicon-chevron-up"></i></span> 
{{headerMarkup}}
 </h4>
    </div>
    <div id="collapseToc{{idx}}" class="panel-collapse collapse">
      <div class="panel-body">)";
  /// @brief closing tags for the preamble
  std::string bodyEnd = R"(
    </div>
  </div>
</div>)";

};

/*! @brief Replaces all the strings with another
*  @param str source content string
*  @param from the original string to be replaced
*  @param to the end string
*  @return modified string */
std::string replaceAll(std::string const& str, std::string const &from, std::string const &to);

/*! @brief Replaces the first string with another
*  @param str source content string
*  @param from the original string to be replaced
*  @param to the end string
*  @return modified string */
std::string replaceFirst(std::string const& str, std::string const &from, std::string const  &to);

/*! @brief Each chapter in the TableOfContents must be enclosed with a Bootstrap 3 accordion
*  @param fileContents the string of html content that contains the table environment
*  @return string with new changed content */
std::string fixToc(std::string const &fileContents);

/*! @brief Find the TableOfContents in the file and extract it
*  @param fileContents the string of html content 
*  @return string with new changed content */
std::string extractToc(std::string const &fileContents);

/*! @brief Enclose all tables with <div class="table-responsive"> and </div>
 *  @param fileContents the string of html content that contains the table environment
 *  @return string with new changed content */
std::string replaceTableWithReponsive(std::string const &fileContents);

/*! @brief Reads a file into a string
 *  @param infile input file stream
 *  @return file contents in string */
std::string loadFile(std::ifstream &infile);

/*! @brief Writes string to a file
 *  @param fileName name with path of the file
 *  @param contents */
void outputFile(std::string const& fileName, std::string const &contents);

/*! @brief Replaces TableOfContents with Accordion and returns fixed one
*  @param contents */
std::string fixTableOfContents(std::string const &contents);

/*! @brief Replaces Go To Top links with section/chapter to Logo
*  @param contents */
std::string fixGoTotop(std::string const&contents);

int main(int argc, char* argv[]){
  std::cout << argv[0];
  if (argc == 2)
  {
    std::cout << "Not enough arguments." << std::endl;
    exit(1);
  }
  else
  {
    std::string fileName = argv[1];
    std::string outputFileName = argv[2];
    std::ifstream infile(fileName);
    if (infile) {
      auto contents = loadFile(infile);
      contents = replaceTableWithReponsive(contents);
      contents = fixTableOfContents(contents);
      contents = fixGoTotop(contents);
      outputFile(outputFileName, contents);
    }
    else {
      std::cout << "file not found!\n";
      return 1;
    }
  }
   return 0 ;
}
std::string fixGoTotop(std::string const&contents) {
  size_t pos = 0;
  std::string retStr(contents);
  std::string findStr = "Go to Top</a>", 
    insertStr = R"(<a href="#claudiordgzLogo" class="btn btn-default pull-right"><span class="glyphicon glyphicon-arrow-up"></span> )";
  while ((pos = retStr.find(findStr, pos)) != std::string::npos) {
    size_t beginPos = retStr.rfind("<a", pos);
    retStr.replace(retStr.begin() + beginPos, retStr.begin() + pos, insertStr);
    pos += insertStr.length() + findStr.length();
  }
  return retStr;
}
std::string fixTableOfContents(std::string const &contents){
  std::string toc = extractToc(contents);
  std::string fixedToc = fixToc(toc);
  return replaceFirst(contents, toc, fixedToc);
}
std::string extractToc(std::string const &fileContents) {
  std::string beginStr = R"(<div class="tableofcontents">)";
  size_t beginPos = fileContents.find(beginStr);
  std::string returnStr("");
  if (beginPos != std::string::npos){
    std::string endStr = R"(<div class="col-md-7" id="docBody">)";
    size_t endPos = fileContents.find(endStr, beginPos);
    if (endPos != std::string::npos) 
      returnStr.append(fileContents.begin() + beginPos, fileContents.begin() + endPos);
  }
  return returnStr;
}
void outputFile(std::string const& fileName, std::string const &contents) {
  std::ofstream out(fileName);
  std::copy(contents.begin(), contents.end(), std::ostreambuf_iterator<char>(out));
}
std::string loadFile(std::ifstream &infile) {
  std::string fileData((std::istreambuf_iterator<char>(infile)),
  std::istreambuf_iterator<char>());
  infile.close();
  return fileData;
}
std::string replaceAll(std::string const& str, std::string const &from, std::string const &to) {
  std::string retStr(str);
  if (!from.empty()) {
    size_t start_pos = 0;
    while ((start_pos = retStr.find(from, start_pos)) != std::string::npos) {
      retStr.replace(start_pos, from.length(), to);
      start_pos += to.length();
    }
  }
  return retStr;
}
std::string replaceFirst(std::string const& str, std::string const &from, std::string const  &to) {
  std::string retStr(str);
  if (!from.empty()) {
    size_t start_pos = retStr.find(from);
    if (start_pos != std::string::npos) {
      retStr.replace(start_pos, from.length(), to);
    }
  }
  return retStr;
}
std::string fixToc(std::string const &tableOfContents){
  size_t beginPos = 0, counter = 1;
  std::string content(tableOfContents);
  std::string findStr = R"(<span class="chapterToc")", endStr = R"(</span>)";
  tocElement instance;
  std::string insertStr(instance.bodyEnd);
  while ((beginPos = content.find(findStr, beginPos)) != std::string::npos) {
    if (counter > 1){
      content.insert(beginPos, insertStr);
      beginPos += insertStr.length();
    }
    else {
      content.insert(beginPos, instance.globalHeaderBegin);
      beginPos += instance.globalHeaderBegin.length();
    }
    size_t endingPos = content.find(endStr, beginPos);
    if (endingPos != std::string::npos) {
      std::string localHeader = instance.header;
      std::string title(content.begin() + beginPos, content.begin() + endingPos + endStr.length());
      localHeader = replaceAll(localHeader, "{{idx}}", std::to_string(counter));
      localHeader = replaceFirst(localHeader, "{{headerMarkup}}", title);
      content = replaceFirst(content, title, localHeader);
      beginPos = content.find(localHeader) + localHeader.length();
      counter++;
    }
    else {
      // parsing error
    }
  }
  content.append(insertStr);
  content.append(instance.globalHeaderEnd);
  return content;
}
std::string replaceTableWithReponsive(std::string const &fileContents) {
  size_t pos = 0;
  std::string content(fileContents);
  std::string findStr = R"(<table)", insertStr = R"(<div class="table-responsive">)";
  while ((pos = content.find(findStr, pos)) != std::string::npos) {
    content.insert(pos, insertStr);
    std::string endStr = R"(</table>)", insertCloseStr = R"(</div>)";
    size_t endingPos = content.find(endStr, pos);
    if (endingPos != std::string::npos) {
      endingPos = endingPos + endStr.length();
      content.insert(endingPos, insertCloseStr);
    }
    pos += insertStr.length() + findStr.length();
  }  
  return content;
}