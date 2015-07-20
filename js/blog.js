/* swap open/close side menu icons */
var StudySeries = {
    init: function(self) {
        this.CodeTogglingHandling().init();
        this.CreateToc().init();
    },
    CreateToc: function() {
      return {
          container: '<div class="mdl-layout--large-screen-only mdl-layout__tab-bar mdl-js-ripple-effect mdl-color--primary-dark">{element}</div>',
          element: '<a href="{{id}}" class="mdl-layout__tab">{{name}}</a>',
          init: function() {
              var domClasses = document.getElementsByClassName('chapterToc'),
                  tocArray = [],
                  first_el = true;
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
                              var newlink = document.createElement('a');
                              newlink.setAttribute('class', 'mdl-layout__tab');
                              newlink.setAttribute('href', idChapterName);
                              newlink.innerHTML = chapterName;
                              if(first_el) {
                                newlink.className += ' is_active';
                                first_el = false;
                              }
                              tocArray.push(newlink.outerHTML);
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

