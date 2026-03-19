

# any

Returns true if array has at least one element.

```kotlin
fun <T> Array<out T>.any(): Boolean(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30)
    println(numbers.any()) // true

    val empty = emptyArray<Int>()
    println(empty.any()) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/any.html)

    