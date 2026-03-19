

# contentDeepHashCode

Returns a hash code based on the contents of this array as if it is List. Nested arrays are treated as lists too.

```kotlin
expect fun <T> Array<out T>.contentDeepHashCode(): Int(source)
```

```kotlin
fun main() {
    val nested = arrayOf(
        arrayOf(1, 2, 3),
        arrayOf(4, 5, 6),
        arrayOf(arrayOf(7, 8), arrayOf(9, 10))
    )

    val hash = nested.contentDeepHashCode()
    println("contentDeepHashCode: $hash")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/content-deep-hash-code.html)

    