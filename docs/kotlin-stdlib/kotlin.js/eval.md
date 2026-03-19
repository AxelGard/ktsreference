

# eval

Exposes the JavaScript eval function to Kotlin.

```kotlin
external fun eval(expr: String): dynamic(source)
```

```kotlin
fun main() {
    val jsExpression = "2 + 3 * 4"
    val result = eval(jsExpression) as Int
    println("Result of eval('$jsExpression'): $result") // prints 14
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/eval.html)

    