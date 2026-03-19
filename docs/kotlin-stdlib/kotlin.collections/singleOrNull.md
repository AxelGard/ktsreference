

# singleOrNull

Returns single element, or null if the array is empty or has more than one element.

```kotlin
fun <T> Array<out T>.singleOrNull(): T?(source)
```

```kotlin
fun main() {
    val singleArray = arrayOf(10)
    println(singleArray.singleOrNull()) // prints: 10

    val multipleArray = arrayOf(1, 2)
    println(multipleArray.singleOrNull()) // prints: null

    val emptyArray = arrayOf<Int>()
    println(emptyArray.singleOrNull()) // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/single-or-null.html)

    