

# jsTypeOf

Function corresponding to JavaScript's typeof operator

```kotlin
external fun jsTypeOf(a: Any?): String(source)
```

```kotlin
import kotlin.js.*

fun main() {
    val number = 42
    val text = "Hello, Kotlin/JS!"
    val flag = true
    val array = arrayOf(1, 2, 3)
    val obj = js("{}")

    println(jsTypeOf(number)) // "number"
    println(jsTypeOf(text))   // "string"
    println(jsTypeOf(flag))   // "boolean"
    println(jsTypeOf(array))  // "object"
    println(jsTypeOf(obj))    // "object"
    println(jsTypeOf(null))   // "object"   // typeof null is "object" in JavaScript
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/js-type-of.html)

    