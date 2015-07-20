/* swap open/close side menu icons */
var StudySeries = {
    init: function(self) {
        this.CodeTogglingHandling().init();
        this.CreateToc().init();
    },
    CreateToc: function() {
      return {
          container: '<div class="mdl-layout__tab-bar-container"><div class="mdl-layout__tab-bar-button mdl-layout__tab-bar-left-button"><i class="material-icons">chevron_left</i></div><div class="mdl-layout__tab-bar mdl-js-ripple-effect mdl-color--primary-dark mdl-js-ripple-effect--ignore-events" data-upgraded=",MaterialRipple">{element}</div><div class="mdl-layout__tab-bar-button mdl-layout__tab-bar-right-button"><i class="material-icons">chevron_right</i></div></div>',
          element: '<a href="{{id}}" class="mdl-layout__tab">{{name}}<span class="mdl-layout__tab-ripple-container mdl-js-ripple-effect" data-upgraded=",MaterialRipple"><span class="mdl-ripple is-animating" style="width: 268.063079926547px; height: 268.063079926547px; -webkit-transform: translate(-50%, -50%) translate(19px, 44px); transform: translate(-50%, -50%) translate(19px, 44px);"></span></span></a>',
          init: function() {
              var domClasses = document.getElementsByClassName('chapterToc'),
                  tocArray = [];
              for(var i = 0; i < domClasses.length; ++i) {
                  for (var j = 0, childNode; j < domClasses[i].childNodes.length; j++) {
                      childNode = domClasses[i].childNodes[j];
                      if(childNode.innerHTML) {
                          var chapterName = childNode.innerHTML,
                              idChapterName = childNode.getAttribute('href');
                              var tocElement = Mustache.to_html(this.element, {
                                  id: idChapterName,
                                  name: chapterName
                              });
                              tocArray.push(tocElement);
                      }
                  }
              }
              var str = tocArray.join("");
              var tocBar = Mustache.to_html(this.container);
              tocBar = tocBar.replace(/{element}/, str);
              document.getElementsByTagName('header')[0].innerHTML += tocBar;
          }
      }
    },

    CodeTogglingHandling: function() {
        return {
            init: function () {
                var domClasses = document.getElementsByClassName('expand-code');
                for (var i = 0; i < domClasses.length; i++) {
                    domClasses[i].addEventListener('click', this, false);
                }
            },
            handleEvent: function (event) {
                switch (event.type) {
                    case "click":
                        this.button(event);
                        break;
                }
            },
            button: function (event) {
                if (/chevron/.test(event.target.className)) {
                    this.expandCollapseCode(event.target);
                } else {
                    var iterable = event.target.parentNode;
                    for (var i = 0, childNode; i <= iterable.childNodes.length; i++) {
                        childNode = iterable.childNodes[i];
                        if (childNode) {
                            if (/pull-right/.test(childNode.className)) {
                                var icon = childNode.childNodes[0];
                                this.expandCollapseCode(icon);
                            }
                        }
                    }
                }
            },
            expandCollapseCode: function (domElement) {
                StudySeries.toggleElementsFromClassNames(domElement, 'fa-chevron-up', 'fa-chevron-down');
            }
        }
    },

    toggleElementsFromClassNames: function(domElement, firstToggle, secondToggle) {
        var regexOne = new RegExp(firstToggle),
            regexTwo = new RegExp(secondToggle);
        if (regexOne.test(domElement.className)) {
            domElement.className = domElement.className.replace(firstToggle, secondToggle);
        } else if (regexTwo.test(domElement.className)) {
            domElement.className = domElement.className.replace(secondToggle, firstToggle);
        }
    }
};

document.addEventListener("DOMContentLoaded", function(event) {
    StudySeries.init(this);
});

