import os
import sys

TARGET:str      = "example-template/index.html";
TARGET_OUT:str  = "index-copy.html";


class AutomakeTemplateStatic:
    def __init__(self, file:str, targetFile:str) -> None:
        self.file:str = file;
        self.targetFile:str = targetFile;

    def readFile(self) -> str:
        with open(self.file, "r+", encoding="utf8") as f:
            return f.read();

    def writeFile(self, content:str):
        with open(self.targetFile, "w+", encoding="utf8") as f:
            f.write(content);
        return;

    def main(self):
        content = self.readFile();
        content = ("{% load static %}\n" if not content.startswith("{% load static %}") else "") + content;
        contentReplaced = content.split("\n");
        replaceStart:int = -1;
        replaceEnd:int = -1;
        print("\n" + ("-" * len(self.file)) + ("\n" * 2) + (self.file.upper()) + ("\n" * 2) + ("-" * len(self.file)))
        for line, i3 in zip(contentReplaced, range(len(contentReplaced))):
            for column, i in zip(line, range(len(line))):
                tagLength = i+5 if any(x in line[i:i+5] for x in ["href =", "href="]) else i + 4 if any(x in line[i:i+4] for x in ["src =", "src="]) else -1;
                if (tagLength < 0):
                    continue;
                print(str(i3) + (" " * (len(str(len(contentReplaced))) - len(str(i3))+2 ))+"|", line[i:(i+5 if line[i+5] == "\"" else i+4)], end="")
                i2:int = tagLength;
                quoteStart:int = -1;
                quoteEnd:int = -1;
                while quoteStart < 0:
                    if (line[i2] == "\""):
                        quoteStart = i2;
                        replaceStart = i2;
                        continue;
                    if (line[i2] in [">", "/>"]):
                        raise SyntaxError(i2);
                    if (i2 == len(content) -1): raise ValueError(i2); 
                    i2+=1;
                i2+=1;
                while quoteEnd < 0:
                    if (line[i2] == "\""):
                        quoteEnd = i2
                        replaceEnd = i2;
                        continue;
                    if (line[i2] in ["<",]):
                        raise SyntaxError(i2);
                    if (i2 == len(content) -1): raise ValueError(i2); 
                    i2+=1;
                replaceStart += 1;
                print(f"\"{line[replaceStart:replaceEnd]}\"");
                if (replaceStart != replaceEnd and (not any(line[replaceStart:replaceEnd].startswith(x) for x in ["#", "https://", "http://", "{"])) and (not any(line[replaceStart:replaceEnd].endswith(x) for x in [".html", "#", ";", "}"])) ):
                    contentReplaced[i3] = line[:replaceStart] + "{"+f"% static '{line[replaceStart:replaceEnd]}' %"+"}" + line[replaceEnd:];
        self.writeFile("".join(line + "\n" for line in contentReplaced)[:-1])                
if __name__ == "__main__":
    if (len(sys.argv)>1):
        for file in os.listdir(sys.argv[1]):
            sys.argv[1] = sys.argv[1][:-1] if any(sys.argv[1][-1] == x for x in ["/", "\\"]) else sys.argv[1]; 
            absPath = sys.argv[1]+"/"+file;
            if (file.endswith(".html") and os.path.isfile(absPath)):
                AutomakeTemplateStatic(absPath, absPath).main();
        exit();
    AutomakeTemplateStatic(TARGET, TARGET_OUT).main();