

# toList

Returns a List containing all elements.

```kotlin
fun <T> Array<out T>.toList(): List<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4)
    val numberList = numbers.toList()
    println(numberList)  // Output: [1, 2, 3, 4]
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-list.html)

    