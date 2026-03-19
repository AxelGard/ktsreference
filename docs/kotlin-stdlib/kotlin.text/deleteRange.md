

# deleteRange

Removes characters in the specified range from this string builder and returns this instance.

```kotlin
@IgnorableReturnValueexpect fun StringBuilder.deleteRange(startIndex: Int, endIndex: Int): StringBuilder(source)
```

```kotlin
fun main() {
    val sb = StringBuilder("Hello, world!")
    sb.deleteRange(5, 12)   // removes ", world"
    println(sb)             // prints: Hello!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/delete-range.html)

    