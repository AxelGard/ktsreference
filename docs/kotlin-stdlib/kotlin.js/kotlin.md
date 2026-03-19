

# kotlin

Obtains a KClass instance for the given constructor reference.

```kotlin
val <T : Any> JsClass<T>.kotlin: KClass<T>(source)
```

```kotlin
import kotlin.js.JsName
import kotlin.js.JsClass
import kotlin.reflect.KClass

// Assume this JavaScript class exists in the global scope.
@JsName("MyJsClass")
external class MyJsClass(val name: String)

fun main() {
    // `MyJsClass` is a reference to the JavaScript constructor.
    val jsCtor: JsClass<MyJsClass> = MyJsClass

    // Obtain the Kotlin KClass for the JavaScript class.
    val kClass: KClass<MyJsClass> = jsCtor.kotlin

    println(kClass.simpleName)   // Prints: MyJsClass
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/kotlin.html)

    