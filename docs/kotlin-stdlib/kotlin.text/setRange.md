

# setRange

Replaces characters in the specified range of this string builder with characters in the specified string value and returns this instance.

```kotlin
@IgnorableReturnValueexpect fun StringBuilder.setRange(startIndex: Int, endIndex: Int, value: String): StringBuilder(source)
```

```kotlin
fun main() {
    val sb = StringBuilder("Hello, World!")
    sb.setRange(7, 12, "Kotlin")
    println(sb) // Output: Hello, Kotlin!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/set-range.html)

    