"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[937],{3905:(e,t,n)=>{n.d(t,{Zo:()=>h,kt:()=>d});var a=n(7294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var l=a.createContext({}),u=function(e){var t=a.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},h=function(e){var t=u(e.components);return a.createElement(l.Provider,{value:t},e.children)},c="mdxType",p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,o=e.originalType,l=e.parentName,h=s(e,["components","mdxType","originalType","parentName"]),c=u(n),m=r,d=c["".concat(l,".").concat(m)]||c[m]||p[m]||o;return n?a.createElement(d,i(i({ref:t},h),{},{components:n})):a.createElement(d,i({ref:t},h))}));function d(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=n.length,i=new Array(o);i[0]=m;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s[c]="string"==typeof e?e:r,i[1]=s;for(var u=2;u<o;u++)i[u]=n[u];return a.createElement.apply(null,i)}return a.createElement.apply(null,n)}m.displayName="MDXCreateElement"},6530:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>p,frontMatter:()=>o,metadata:()=>s,toc:()=>u});var a=n(7462),r=(n(7294),n(3905));const o={},i="Scam",s={unversionedId:"Challenges/Scam",id:"Challenges/Scam",title:"Scam",description:"Difficulty: \u2b50\u2b50\u2b50",source:"@site/docs/Challenges/3. Scam.md",sourceDirName:"Challenges",slug:"/Challenges/Scam",permalink:"/PythonTutorial/docs/Challenges/Scam",draft:!1,editUrl:"https://github.com/JaedanC/PythonTutorial/tree/main/docs/Challenges/3. Scam.md",tags:[],version:"current",sidebarPosition:3,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Crosswords",permalink:"/PythonTutorial/docs/Challenges/Crosswords"},next:{title:"Secret Message",permalink:"/PythonTutorial/docs/Challenges/SecretMessage"}},l={},u=[{value:"The Game",id:"the-game",level:2},{value:"You are Tim",id:"you-are-tim",level:2},{value:"Useful Functions",id:"useful-functions",level:2},{value:"Regarding Security",id:"regarding-security",level:2}],h={toc:u},c="wrapper";function p(e){let{components:t,...n}=e;return(0,r.kt)(c,(0,a.Z)({},h,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"scam"},"Scam"),(0,r.kt)("admonition",{type:"note"},(0,r.kt)("p",{parentName:"admonition"},"Difficulty: \u2b50\u2b50\u2b50")),(0,r.kt)("p",null,"This is a security question."),(0,r.kt)("h2",{id:"the-game"},"The Game"),(0,r.kt)("p",null,"Tim is trying to scam people of bitcoin on the internet. He is doing this by running a challenge. People have got to try and guess the answer to a question. If they don't guess correctly he wins."),(0,r.kt)("blockquote",null,(0,r.kt)("p",{parentName:"blockquote"},"My favourite number is: ",(0,r.kt)("strong",{parentName:"p"},"_"))),(0,r.kt)("p",null,"Tim is going to scam people by having two answers to the question, and he'll reveal the real answer second."),(0,r.kt)("p",null,"To prove to people that he has the right answer, he first ",(0,r.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/Cryptographic_hash_function"},"hashes")," his answer and posts it publically on the internet. Then, he allows the challenge to run for a week. Each person should try to guess the number, and then will hash their answer to see if they have the right answer."),(0,r.kt)("h2",{id:"you-are-tim"},"You are Tim"),(0,r.kt)("p",null,"Your job is to find two answers to the question that share the same hash. Now, since we will use ",(0,r.kt)("a",{parentName:"p",href:"https://www.geeksforgeeks.org/md5-hash-python/"},"MD5")," to hash and finding duplicate hashes is very hard, treat the two hashes as a match if they have the same first 12 characters in the hash."),(0,r.kt)("admonition",{type:"note"},(0,r.kt)("p",{parentName:"admonition"},"You must hash the entire sentence, not just the number.")),(0,r.kt)("p",null,"For example:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-txt"},"My favourite number is: 25874428\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-txt"},"78a7dcde58c5b4d28f3acdfb4cf9741f\n")),(0,r.kt)("p",null,"And another answer"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-txt"},"My favourite number is: 20609915\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-txt"},"78a7dcde58c53d7b58f7b28da16f793c\n")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Notice how the first 12 characters are the same."),(0,r.kt)("li",{parentName:"ul"},"A solution to this question would then be 25874428 and 20609915.")),(0,r.kt)("p",null,"The example above is real. Your job is to find another one. ",(0,r.kt)("em",{parentName:"p"},"I deliberately started at a random high number in the example. Your code can just start searching from 0 if you want.")),(0,r.kt)("p",null,"Your program must find two integers that satisfy the requirements. You are not required to be able to ",(0,r.kt)("em",{parentName:"p"},"play")," the scam. Use a ",(0,r.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/Birthday_attack"},"birthday attack")," to try and find some matches."),(0,r.kt)("h2",{id:"useful-functions"},"Useful Functions"),(0,r.kt)("p",null,"Some useful functions for this task are:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"hashlib.md5()")," (",(0,r.kt)("inlineCode",{parentName:"li"},"import hashlib")," first)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"_Hash.hexdigest()")," (Method. On the return result of above)"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"str.encode()")," (Encode method on strings)")),(0,r.kt)("h2",{id:"regarding-security"},"Regarding Security"),(0,r.kt)("admonition",{type:"caution"},(0,r.kt)("p",{parentName:"admonition"},"The hashing algorithm of ",(0,r.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/MD5"},"MD5")," is considered broken because it is easy to generate two hashes that are completely identical with a bit of understanding of how the algorithm works. For this reason, MD5 is generally avoided. It is much more common to see ",(0,r.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/SHA-2"},"SHA256")," being used."),(0,r.kt)("p",{parentName:"admonition"},"This challenge does not expose this flaw. I chose MD5 because it is included in base python. SHA256 requires external libraries to use. If you wanted to use a secure hashing function, then it is important to research the currently accepted hashing algorithms. It's also important that you ",(0,r.kt)("strong",{parentName:"p"},"don't")," try to implement them yourselves. Use a trusted library.")))}p.isMDXComponent=!0}}]);