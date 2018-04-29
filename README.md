# DesignPatternAlex
### Content
+ Abstract Factory
+ Adapter
+ Bridge
+ Builder
+ Chain Of Responsibility
+ Composite
+ Decorator
+ Facade
+ Factory Method
+ Flyweight
+ Observer
+ Proxy
+ Simple Factory
+ Singleton
+ Strategy
+ Template Method

### Directory Structure
```
.
├── .git
│   ├── HEAD
│   ├── branches
│   ├── config
│   ├── description
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   └── update.sample
│   ├── info
│   │   └── exclude
│   ├── objects
│   │   ├── info
│   │   └── pack
│   └── refs
│       ├── heads
│       └── tags
├── .idea
│   ├── DisgnPattern.iml
│   ├── inspectionProfiles
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   ├── modules.xml
│   └── workspace.xml
├── AbstractFactory.png
├── AbstractFactory.py
├── Adapter.png
├── Adapter.py
├── Bridge.png
├── Bridge.py
├── Builder.png
├── Builder.py
├── ChainOfResponsibility.png
├── ChainOfResponsibility.py
├── Composite.png
├── Composite.py
├── Decorator.png
├── Decorator.py
├── Facade.png
├── Facade.py
├── FactoryMethod.png
├── FactoryMethod.py
├── Flyweight.png
├── Flyweight.py
├── Observer.png
├── Observer.py
├── Proxy.png
├── Proxy.py
├── README.md
├── SimpleFactory.png
├── SimpleFactory.py
├── Singleton.png
├── Singleton.py
├── Strategy.png
├── Strategy.py
├── TemplateMethod.png
└── TemplateMethod.py
```
### Example 
* Codes
``` python
import time


class foo(object):
    def f1(self):
        print("Original f1")

    def f2(self):
        print("Original f2")


class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print(
            'decorated f1 @ %s.' % time.strftime(
                '%Y/%m/%d %H:%M:%S', time.localtime()
            )
        )
        self._decoratee.f1()

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


u = foo()
v = foo_decorator(u)  # v为修饰u后的结果

v.f1()
v.f2()
```