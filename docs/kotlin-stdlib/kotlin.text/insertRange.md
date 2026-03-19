

# insertRange

Inserts characters in a subarray of the specified character array value into this string builder at the specified index and returns this instance.

```kotlin
@IgnorableReturnValueexpect fun StringBuilder.insertRange(index: Int, value: CharArray, startIndex: Int, endIndex: Int): StringBuilder(source)
```

```kotlin
fun main() {
    val sb = StringBuilder("Hello")
    val chars = " Kotlin".toCharArray()
    sb.insertRange(5, chars, 0, chars.size) // inserts " Kotlin" at position 5
    println(sb)   // Output: Hello Kotlin
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/insert-range.html)

    