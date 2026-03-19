

# contentDeepEquals

Checks if the two specified arrays are deeply equal to one another.

```kotlin
expect infix fun <T> Array<out T>.contentDeepEquals(other: Array<out T>): Boolean(source)
```

```kotlin
fun main() {
    val nested1 = arrayOf(arrayOf(1, 2), arrayOf(3, 4))
    val nested2 = arrayOf(arrayOf(1, 2), arrayOf(3, 4))
    val nested3 = arrayOf(arrayOf(1, 2), arrayOf(4, 3))

    println(nested1 contentDeepEquals nested2) // true
    println(nested1 contentDeepEquals nested3) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/content-deep-equals.html)

    