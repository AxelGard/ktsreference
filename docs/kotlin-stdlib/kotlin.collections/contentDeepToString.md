

# contentDeepToString

Returns a string representation of the contents of this array as if it is a List. Nested arrays are treated as lists too.

```kotlin
expect fun <T> Array<out T>.contentDeepToString(): String(source)
```

```kotlin
fun main() {
    val nestedArray = arrayOf(
        arrayOf(1, 2),
        arrayOf(3, 4, arrayOf(5, 6))
    )

    println(nestedArray.contentDeepToString())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/content-deep-to-string.html)

    