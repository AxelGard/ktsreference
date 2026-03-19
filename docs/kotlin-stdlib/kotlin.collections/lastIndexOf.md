

# lastIndexOf

Returns last index of element, or -1 if the array does not contain element.

```kotlin
fun <T> Array<out T>.lastIndexOf(element: T): Int(source)
```

```kotlin
val fruits = arrayOf("apple", "banana", "apple", "cherry")

val lastIndex = fruits.lastIndexOf("apple")
println("Last index of \"apple\" is $lastIndex")  // Output: Last index of "apple" is 2
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/last-index-of.html)

    