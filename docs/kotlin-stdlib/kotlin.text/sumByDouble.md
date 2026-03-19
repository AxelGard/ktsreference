

# sumByDouble

Warning since 1.5

```kotlin
inline fun CharSequence.sumByDouble(selector: (Char) -> Double): Double(source)
```

```kotlin
fun main() {
    val text = "kotlin"
    val sum = text.sumByDouble { it.code.toDouble() }
    println("Sum of character codes in \"$text\" is $sum")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/sum-by-double.html)

    