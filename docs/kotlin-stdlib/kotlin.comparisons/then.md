

# then

Combines this comparator and the given comparator such that the latter is applied only when the former considered values equal.

```kotlin
infix fun <T> Comparator<T>.then(comparator: Comparator<in T>): Comparator<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = listOf(
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Alice", 20),
        Person("Bob", 20),
        Person("Charlie", 35)
    )

    val comparator = compareBy<Person> { it.name }
        .then(compareBy { it.age })

    val sorted = people.sortedWith(comparator)

    sorted.forEach { println("${it.name} (${it.age})") }
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/then.html)

    