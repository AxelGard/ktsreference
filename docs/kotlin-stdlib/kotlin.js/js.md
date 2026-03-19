

# js

Puts the given piece of a JavaScript code right into the calling function. The compiler replaces call to js(...) code with the string constant provided as a parameter.

```kotlin
actual external fun js(code: String): dynamic(source)
```

```kotlin
fun main() {
    // Get the page title using JavaScript
    val title: String = js("document.title")
    println("Page title: $title")

    // Evaluate a JavaScript expression
    val sum: Int = js("1 + 2")
    println("1 + 2 = $sum")

    // Execute a JavaScript snippet with a side effect
    js("console.log('Hello from Kotlin JS')")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/js.html)

    