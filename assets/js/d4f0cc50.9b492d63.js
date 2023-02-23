"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[798],{3905:(e,t,r)=>{r.d(t,{Zo:()=>u,kt:()=>m});var n=r(7294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var s=n.createContext({}),p=function(e){var t=n.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},u=function(e){var t=p(e.components);return n.createElement(s.Provider,{value:t},e.children)},c="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},h=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,a=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),c=p(r),h=o,m=c["".concat(s,".").concat(h)]||c[h]||d[h]||a;return r?n.createElement(m,i(i({ref:t},u),{},{components:r})):n.createElement(m,i({ref:t},u))}));function m(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=r.length,i=new Array(a);i[0]=h;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l[c]="string"==typeof e?e:o,i[1]=l;for(var p=2;p<a;p++)i[p]=r[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}h.displayName="MDXCreateElement"},8975:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>d,frontMatter:()=>a,metadata:()=>l,toc:()=>p});var n=r(7462),o=(r(7294),r(3905));const a={},i="Crosswords",l={unversionedId:"Challenges/Crosswords",id:"Challenges/Crosswords",title:"Crosswords",description:"Difficulty: \u2b50\u2b50",source:"@site/docs/Challenges/2. Crosswords.md",sourceDirName:"Challenges",slug:"/Challenges/Crosswords",permalink:"/PythonTutorial/docs/Challenges/Crosswords",draft:!1,editUrl:"https://github.com/JaedanC/PythonTutorial/tree/main/docs/Challenges/2. Crosswords.md",tags:[],version:"current",sidebarPosition:2,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Rot13",permalink:"/PythonTutorial/docs/Challenges/Rot13"},next:{title:"Scam",permalink:"/PythonTutorial/docs/Challenges/Scam"}},s={},p=[{value:"Solving for words",id:"solving-for-words",level:2}],u={toc:p},c="wrapper";function d(e){let{components:t,...r}=e;return(0,o.kt)(c,(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"crosswords"},"Crosswords"),(0,o.kt)("admonition",{type:"note"},(0,o.kt)("p",{parentName:"admonition"},"Difficulty: \u2b50\u2b50")),(0,o.kt)("p",null,"Write a python program that assists in solving for words in a crossword. This is done by inputing what the known characters are for a word, and then the program will print a list of possible words that could go in that spot. Execution of the program is as follows:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"$ python crossword.py <path-to-word-list>\n")),(0,o.kt)("p",null,"The ",(0,o.kt)("inlineCode",{parentName:"p"},"crossword.py")," file will contain the code for the program. The word-list file will be a file I will provide to you. For context, the word list file is just a standard .txt file that usually comes with linux computers that includes all English words in the dictionary. I will send you this file. Treat this dictionary as the possible solutions for a word in the crossword."),(0,o.kt)("h2",{id:"solving-for-words"},"Solving for words"),(0,o.kt)("p",null,"When the program is run initially print out some useful information to the user on how to use the program. Below is an example but, it is not exhaustive by any means."),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"$ python crossword.py words.txt\nPlease input your word by typing the known letters and \u2018?\u2019 where you do not know the\nletter.\n")),(0,o.kt)("p",null,"Then, to solve a word the user will be asked to include some input. Print the \u201c>\u201d character to tell the user we are waiting for some input (highlighted in green is text input by the user in this example)."),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"> tr??n\ntrain\ntreen\n> bre???t?\nbregmata\nbreviate\n>\n")),(0,o.kt)("p",null,"The program will continue to ask for words. In the example above you can see that one of the user inputs was the word \u201ctr??n\u201d. And it matched two words in the dictionary, so it printed them both out. Note that the number of letters must match as well. The program will close when the user press CTRL+C. (This is the standard way of telling a program to die)."),(0,o.kt)("p",null,"These are the concepts that will need to be researched to do this task, in order of how they should be researched:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Variables"),(0,o.kt)("li",{parentName:"ul"},"If statements."),(0,o.kt)("li",{parentName:"ul"},"Printing"),(0,o.kt)("li",{parentName:"ul"},"Command-line arguments"),(0,o.kt)("li",{parentName:"ul"},"Opening and reading text files"),(0,o.kt)("li",{parentName:"ul"},"String manipulation"),(0,o.kt)("li",{parentName:"ul"},"User input"),(0,o.kt)("li",{parentName:"ul"},"While loops")),(0,o.kt)("p",null,"I recommend not trying to tackle the program instantly, but rather become familiar with the concepts above before trying to attempt the problem."))}d.isMDXComponent=!0}}]);