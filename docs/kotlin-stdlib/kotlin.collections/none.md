

# none

Returns true if the array has no elements.

```kotlin
fun <T> Array<out T>.none(): Boolean(source)
```

```kotlin
fun main() {
    val emptyArray = emptyArray<Int>()
    println(emptyArray.none()) // true

    val nonEmptyArray = arrayOf(1, 2, 3)
    println(nonEmptyArray.none()) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/none.html)

    