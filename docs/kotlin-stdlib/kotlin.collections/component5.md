

# component5

Returns 5th element from the array.

```kotlin
inline operator fun <T> Array<out T>.component5(): T(source)
```

```kotlin
fun main() {
    val arr = arrayOf("a", "b", "c", "d", "e")
    val fifth = arr.component5()
    println(fifth) // Output: e
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/component5.html)

    