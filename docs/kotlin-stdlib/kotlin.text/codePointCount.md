

# codePointCount

Returns the number of Unicode code points in the specified text range of this String.

```kotlin
inline fun String.codePointCount(beginIndex: Int, endIndex: Int): Int(source)
```

```kotlin
fun main() {
    val text = "Hello 👋🌍!"
    val totalCodePoints = text.codePointCount(0, text.length)
    println("Total code points: $totalCodePoints")  // prints 9

    val emojiOnly = text.codePointCount(6, text.length)
    println("Code points from index 6: $emojiOnly")   // prints 3
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/code-point-count.html)

    