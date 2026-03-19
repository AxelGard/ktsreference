

# appendRange

Appends a subsequence of the specified character sequence value to this Appendable and returns this instance.

```kotlin
@IgnorableReturnValuefun <T : Appendable> T.appendRange(value: CharSequence, startIndex: Int, endIndex: Int): T(source)
```

```kotlin
fun main() {
    val sb = StringBuilder()
    val source = "Hello, World!"
    sb.appendRange(source, 7, 12) // appends "World"
    println(sb) // prints "World"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/append-range.html)

    