

# count

Returns the number of elements in this array.

```kotlin
inline fun <T> Array<out T>.count(): Int(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30, 40, 50)
    val size = numbers.count()          // size will be 5
    println("Array contains $size elements")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/count.html)

    